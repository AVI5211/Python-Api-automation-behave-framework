from behave import given, when, then
import requests

@given('the user "{user_id}" and the post "{post_id}"')
def step_given_user_and_post(context, user_id, post_id):
    context.user_id = user_id
    context.post_id = post_id

@when('the user comments "{comment}" on the post')
def step_when_user_comments(context, comment):
    url = "http://3.27.18.54/index.php/comment-on-post"
    data = {"userId": context.user_id, "postId": context.post_id, "commentDesc": comment}
    context.comment_response = requests.post(url, data=data)

@when('the user likes the post')
def step_when_user_likes(context):
    url = "http://3.27.18.54/index.php/like-on-post"
    data = {"userId": context.user_id, "postId": context.post_id}
    context.like_response = requests.post(url, data=data)

@then('the comment should be added')
def step_then_comment_added(context):
    assert context.comment_response.status_code == 200

@then('the like should be verified')
def step_then_like_verified(context):
    assert context.like_response.status_code == 200
