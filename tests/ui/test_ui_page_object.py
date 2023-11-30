from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incoorrect_username_page_object():
    #create objects page
    sign_in_page = SignInPage()

    #Open github.com/login
    sign_in_page.go_to()

    #try to login
    sign_in_page.try_login("page_object@gmail.com", "Wrong password")

    #check page title

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #close
    sign_in_page.close()

