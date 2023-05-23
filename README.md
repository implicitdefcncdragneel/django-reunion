# Social Media API

This API provides functionalities for a social media platform, allowing users to manage user profiles, follow other users, upload and delete posts, like and unlike posts, and comment on posts. 

## API Endpoints

### User Authentication

- `POST /api/authenticate`: Performs user authentication and returns a JWT token.
  - Input: Email, Password
  - Return: JWT token

### User Actions

- `POST /api/follow/{id}`: Authenticated user follows a user with the specified ID.
- `POST /api/unfollow/{id}`: Authenticated user unfollows a user with the specified ID.
- `GET /api/user`: Authenticates the request and returns the respective user profile.
  - Return: User Name, Number of followers, Number of followings

### Post Actions

- `POST /api/posts/`: Adds a new post created by the authenticated user.
  - Input: Title, Description
  - Return: Post ID, Title, Description, Created Time (UTC)
- `DELETE /api/posts/{id}`: Deletes the post with the specified ID created by the authenticated user.
- `POST /api/like/{id}`: Likes the post with the specified ID by the authenticated user.
- `POST /api/unlike/{id}`: Unlikes the post with the specified ID by the authenticated user.
- `POST /api/comment/{id}`: Adds a comment for the post with the specified ID by the authenticated user.
  - Input: Comment
  - Return: Comment ID
- `GET /api/posts/{id}`: Returns a single post with the specified ID, including the number of likes and comments.
- `GET /api/all_posts`: Returns all posts created by the authenticated user, sorted by post time.
  - Return: For each post:
    - ID: ID of the post
    - Title: Title of the post
    - Description: Description of the post
    - Created At: Date and time when the post was created
    - Comments: Array of comments for the particular post
    - Likes: Number of likes for the particular post