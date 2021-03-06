from trading_ig.rest import IGService, IGException
import responses
import json
import pytest

"""
unit tests for rest module
"""

# login v1


@responses.activate
def test_login_v1_happy():

    with open('tests/data/accounts.json', 'r') as file:
        response_body = json.loads(file.read())

    responses.add(responses.POST, 'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json=response_body,
                  status=200)

    ig_service = IGService('username','password', 'api_key', 'DEMO')
    result = ig_service.create_session()

    assert result['accountType'] == 'SPREADBET'
    assert result['currentAccountId'] == 'ABC123'
    assert len(result['accounts']) == 2
    assert result['accounts'][1]['accountName'] == 'Demo-cfd'
    assert result['accounts'][1]['accountType'] == 'CFD'
    assert result['trailingStopsEnabled'] == True


@responses.activate
def test_login_v1_bad_api_key():

    responses.add(responses.POST, 'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json={'errorCode': 'error.security.api-key-invalid'},
                  status=403)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(Exception):
        result = ig_service.create_session()
        assert result['errorCode'] == 'error.security.api-key-invalid'


@responses.activate
def test_login_v1_bad_credentials():

    responses.add(responses.POST,
                  'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json={'errorCode': 'error.security.invalid-details'},
                  status=401)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(Exception):
        result = ig_service.create_session()
        assert result['errorCode'] == 'error.security.invalid-details'


@responses.activate
def test_login_v1_encrypted_happy():

    with open('tests/data/accounts.json', 'r') as file:
        response_body = json.loads(file.read())

    responses.add(responses.GET,
                  'https://demo-api.ig.com/gateway/deal/session/encryptionKey',
                  json={
                      'encryptionKey': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp9te7zwed8HhdRFsn47EI8exZ1Yi+bJoKtclGTiuaP1T+4AclNqB2mIya/Ik6IV6A2pt4FFVoqvrhJA46dWi4XgA4Ojhl2Xxw4++blAMgT3jU7N5nY13LdJzZuYv/oPZKRcEj6RrlBV68HjrTnjAMWARl0jFbVCiLWovTGJ0stx/zJAKX0GFyuUlsoaJISJJRYeOLUtZ8Z4BE6ZkmKnz4V8YNyyoWCyXQp+IKCZrfoEdlMOPBgsjbRy02Gh9xZqcm2erLsp40F+w3AjHUqQQi7eQuPQaPWq9Lhm8cVDH2CB2BtfM8Ew8T5/A36eqa5eoeQcZaMnLUQP5UYtG2Wd//wIDAQAB',
                      'timeStamp': '1601218928621'
                  },
                  status=200)

    responses.add(responses.POST,
                  'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json=response_body,
                  status=200)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')
    result = ig_service.create_session(encryption=True)

    assert result['accountType'] == 'SPREADBET'
    assert result['currentAccountId'] == 'ABC123'
    assert len(result['accounts']) == 2
    assert result['accounts'][1]['accountName'] == 'Demo-cfd'
    assert result['accounts'][1]['accountType'] == 'CFD'
    assert result['trailingStopsEnabled'] == True


@responses.activate
def test_login_v1_encrypted_bad_key():

    responses.add(responses.GET,
                  'https://demo-api.ig.com/gateway/deal/session/encryptionKey',
                  json={'errorCode': 'error.security.api-key-invalid'},
                  status=403)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(IGException):
        result = ig_service.create_session(encryption=True)
        assert result['errorCode'] == 'error.security.api-key-invalid'


# login v2


@responses.activate
def test_login_v2_happy():

    with open('tests/data/accounts.json', 'r') as file:
        response_body = json.loads(file.read())

    responses.add(responses.POST, 'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json=response_body,
                  status=200)

    ig_service = IGService('username','password', 'api_key', 'DEMO')
    result = ig_service.create_session()

    assert result['accountType'] == 'SPREADBET'
    assert result['currentAccountId'] == 'ABC123'
    assert len(result['accounts']) == 2
    assert result['accounts'][1]['accountName'] == 'Demo-cfd'
    assert result['accounts'][1]['accountType'] == 'CFD'
    assert result['trailingStopsEnabled'] == True


@responses.activate
def test_login_v2_bad_api_key():

    responses.add(responses.POST, 'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json={'errorCode': 'error.security.api-key-invalid'},
                  status=403)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(Exception):
        result = ig_service.create_session()
        assert result['errorCode'] == 'error.security.api-key-invalid'


@responses.activate
def test_login_v2_bad_credentials():

    responses.add(responses.POST,
                  'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json={'errorCode': 'error.security.invalid-details'},
                  status=401)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(Exception):
        result = ig_service.create_session()
        assert result['errorCode'] == 'error.security.invalid-details'


@responses.activate
def test_login_v2_encrypted_happy():

    with open('tests/data/accounts.json', 'r') as file:
        response_body = json.loads(file.read())

    responses.add(responses.GET,
                  'https://demo-api.ig.com/gateway/deal/session/encryptionKey',
                  json={
                      'encryptionKey': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp9te7zwed8HhdRFsn47EI8exZ1Yi+bJoKtclGTiuaP1T+4AclNqB2mIya/Ik6IV6A2pt4FFVoqvrhJA46dWi4XgA4Ojhl2Xxw4++blAMgT3jU7N5nY13LdJzZuYv/oPZKRcEj6RrlBV68HjrTnjAMWARl0jFbVCiLWovTGJ0stx/zJAKX0GFyuUlsoaJISJJRYeOLUtZ8Z4BE6ZkmKnz4V8YNyyoWCyXQp+IKCZrfoEdlMOPBgsjbRy02Gh9xZqcm2erLsp40F+w3AjHUqQQi7eQuPQaPWq9Lhm8cVDH2CB2BtfM8Ew8T5/A36eqa5eoeQcZaMnLUQP5UYtG2Wd//wIDAQAB',
                      'timeStamp': '1601218928621'
                  },
                  status=200)

    responses.add(responses.POST,
                  'https://demo-api.ig.com/gateway/deal/session',
                  headers = {'CST': 'abc123abc123abc123abc123abc123abc123'},
                  json=response_body,
                  status=200)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')
    result = ig_service.create_session(encryption=True)

    assert result['accountType'] == 'SPREADBET'
    assert result['currentAccountId'] == 'ABC123'
    assert len(result['accounts']) == 2
    assert result['accounts'][1]['accountName'] == 'Demo-cfd'
    assert result['accounts'][1]['accountType'] == 'CFD'
    assert result['trailingStopsEnabled'] == True


@responses.activate
def test_login_v2_encrypted_bad_key():

    responses.add(responses.GET,
                  'https://demo-api.ig.com/gateway/deal/session/encryptionKey',
                  json={'errorCode': 'error.security.api-key-invalid'},
                  status=403)

    ig_service = IGService('username', 'password', 'api_key', 'DEMO')

    with pytest.raises(IGException):
        result = ig_service.create_session(encryption=True)
        assert result['errorCode'] == 'error.security.api-key-invalid'

