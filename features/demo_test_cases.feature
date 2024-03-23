Feature: Automate comments and likes on posts

  Scenario Outline: Comment and like on a post
    Given the user "<user_id>" and the post "<post_id>"
    When the user comments "<comment>" on the post
    And the user likes the post
    Then the comment should be added
    And the like should be verified

    Examples:
      | user_id | post_id | comment       |
      | 2       | 22      | wow you r awsome |
      | 4       | 22      | love you      |
      | 5       | 22      | amazing       |
      | 6       | 22      | well          |
