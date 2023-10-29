import pytest
import requests


@pytest.mark.api
def test_user_exists(github_api):
    
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    
    r = github_api.search_repo('become-qa-auto')
   # print(r)
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r= github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emoji(github_api):
    r = github_api.get_emojis()
    assert r == 200

@pytest.mark.api
def test_emoji_non_correct_url(github_api):

    r = github_api.get_emojis_non_correct('23')
    assert r['message'] == 'Not Found'



@pytest.mark.api
def test_list_commits(github_api):
    r = github_api.list_commits('Disikus','Den_QA-Auto23')
    #assert 'Myrhorodskyi Denys' in  r['author'][0]['name']
    #print(r[0]['author'])
    assert 'Disikus' in r[0]['author']['login']

@pytest.mark.api
def test_list_commits_name(github_api):
    r = github_api.list_commits('Disikus','Den_QA-Auto23')
    #assert 'Myrhorodskyi Denys' in  r['author'][0]['name']
    #print(r[0]['author'])
    assert 'Myrhorodskyi Denys' in r[0]['commit']['author']['name']

@pytest.mark.api
def test_list_commits_exists(github_api):
    r = github_api.list_commits_status_code('Disikus','Den_QA-Auto23')
    assert r == 200

@pytest.mark.api
def test_list_commits_non_exists(github_api):
    r = github_api.list_commits_status_code('Disikus','Den_Q-Auto23')
    assert r == 404

@pytest.mark.api
def test_list_commits_no_repo(github_api):
    r = github_api.list_commits_status_code('Disikus','')
    assert r == 404
    

 

   