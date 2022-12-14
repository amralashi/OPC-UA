import unittest

from opcua import Client
from opcua import Server
from opcua import ua

try:
    from opcua.crypto import uacrypto
    from opcua.crypto import security_policies
except ImportError:
    print("WARNING: CRYPTO NOT AVAILABLE, CRYPTO TESTS DISABLED!!")
    disable_crypto_tests = True
else:
    disable_crypto_tests = False


port_num1 = 48515
port_num2 = 48512
port_num3 = 48510
port_num4 = 48533

@unittest.skipIf(disable_crypto_tests, "crypto not available")
class TestCryptoConnect(unittest.TestCase):

    '''
    Test connectino with a server supporting crypto 

    '''
    @classmethod
    def setUpClass(cls):
        # start our own server
        cls.srv_crypto = Server()
        cls.uri_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num1)
        cls.srv_crypto.set_endpoint(cls.uri_crypto)
        # load server certificate and private key. This enables endpoints
        # with signing and encryption.
        cls.srv_crypto.load_certificate("../examples/certificate-example.der")
        cls.srv_crypto.load_private_key("../examples/private-key-example.pem")
        cls.srv_crypto.start()

        # start a server without crypto
        cls.srv_no_crypto = Server()
        cls.uri_no_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num2)
        cls.srv_no_crypto.set_endpoint(cls.uri_no_crypto)
        cls.srv_no_crypto.start()

        # start server with long key
        cls.srv_crypto2 = Server()
        cls.uri_crypto2 = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num3)
        cls.srv_crypto2.set_endpoint(cls.uri_crypto2)
        cls.srv_crypto2.load_certificate("../examples/certificate-3072-example.der")
        cls.srv_crypto2.load_private_key("../examples/private-key-3072-example.pem")
        cls.srv_crypto2.start()

        cls.srv_crypto_no_anoymous = Server()
        cls.uri_crypto_no_anoymous = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num4)
        cls.srv_crypto_no_anoymous.set_endpoint(cls.uri_crypto_no_anoymous)
        cls.srv_crypto_no_anoymous.load_certificate("examples/certificate-3072-example.der")
        cls.srv_crypto_no_anoymous.load_private_key("examples/private-key-3072-example.pem")
        cls.srv_crypto_no_anoymous.set_security_IDs(["Username", "Basic256Sha256"])
        cls.srv_crypto_no_anoymous.start()

    @classmethod
    def tearDownClass(cls):
        # stop the server 
        cls.srv_no_crypto.stop()
        cls.srv_crypto.stop()
        cls.srv_crypto2.stop()

    def test_nocrypto(self):
        clt = Client(self.uri_no_crypto)
        clt.connect()
        try:
            clt.get_objects_node().get_children()
        finally:
            clt.disconnect()

    def test_nocrypto_fail(self):
        clt = Client(self.uri_no_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security_string("Basic256Sha256,Sign,../examples/certificate-example.der,../examples/private-key-example.pem")

    def test_basic256sha256(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256Sha256,Sign,../examples/certificate-example.der,../examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha256_longkey(self):
        clt = Client(self.uri_crypto2)
        try:
            clt.set_security_string("Basic256Sha256,Sign,../examples/certificate-example.der,../examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha256_encrypt(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256Sha256,SignAndEncrypt,../examples/certificate-example.der,../examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha256_encrypt_longkey(self):
        clt = Client(self.uri_crypto2)
        try:
            clt.set_security_string("Basic256Sha256,SignAndEncrypt,../examples/certificate-example.der,../examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha56_encrypt_success(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security(security_policies.SecurityPolicyBasic256Sha256,
                             '../examples/certificate-example.der',
                             '../examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.SignAndEncrypt
                             )
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha56_encrypt_fail(self):
        # FIXME: how to make it fail???
        clt = Client(self.uri_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security(security_policies.SecurityPolicyBasic256Sha256,
                             '../examples/certificate-example.der',
                             '../examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.None_
                             )

    def test_anonymous_rejection(self):
        # FIXME: how to make it fail???
        clt = Client(self.uri_crypto_no_anoymous)
        with self.assertRaises(ua.UaError) as exc_info:
            clt.connect()
            clt.disconnect()
        assert ua.StatusCodes.BadIdentityTokenRejected == exc_info.type.code
