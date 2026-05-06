import pytest

pytestmark = pytest.mark.ui


def test_admin_and_guest_sessions_are_isolated(user_session_factory):
    admin = user_session_factory("admin")
    guest = user_session_factory("guest")

    admin_role = admin["page"].evaluate(
        "localStorage.getItem('user_role')"
    )

    guest_role = guest["page"].evaluate(
        "localStorage.getItem('user_role')"
    )

    admin_token = admin["page"].evaluate(
        "localStorage.getItem('auth_token')"
    )

    guest_token = guest["page"].evaluate(
        "localStorage.getItem('auth_token')"
    )

    assert admin_role == "admin"
    assert guest_role == "guest"

    assert admin_token == "admin-token-123"
    assert guest_token == "guest-token-456"

    admin["context"].close()
    guest["context"].close()
