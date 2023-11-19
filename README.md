## Goal

The app is designed to achieve the following goals:

-   Provide a centralized platform for anime enthusiasts to discover, track, and engage with anime content.
-   Create a community where users can discuss their favorite anime, share reviews, and recommendations.
-   Offer a personalized experience by allowing users to build and maintain their anime watchlists.
-   Enhance the overall anime-watching experience by providing information on upcoming releases, news, and trends in the anime world.
-   Promote user engagement through features such as user-generated content, comments, and social interactions.
- 
## User Demographics

-   **Age Group:** Primarily, users aged 13 to 35, with a focus on the 18 to 30 demographic, as anime appeals to a wide age range.
-   **Gender:** The user base is expected to be diverse, with a fairly equal split between male and female users.
-   **Interests:** Anime enthusiasts, manga readers, and fans of related Japanese pop culture (e.g., cosplay, conventions).
-   **Geographic Location:** Worldwide, with a significant portion of users in regions where anime is popular, such as Japan, North America, and Europe.

## Data Usage

-   **Anime Database:** Information about anime series, including titles, descriptions, genres, episodes, release dates, and ratings.
-   **User Profiles:** User-generated data like watchlists, reviews, ratings, and comments.
-   **Community Data:** Forum posts, user interactions, and social features.
-   **News and Updates:** Information on upcoming anime releases, industry news, and trends.
-   **User Authentication:** User account data, including email addresses (to be secured).

## Project Approach

### a. Database Schema

-   Tables for anime series, user profiles, reviews, comments, and forum posts.
-   Relationships between users and their watchlists, user-generated content, and user interactions.

### b. API Challenges

-   ~~Finding a reliable anime database API with up-to-date information.~~
-   API to be used: [AnimeDB](https://rapidapi.com/brian.rofiq/api/anime-db/)
-   Handling rate limiting and authentication with the chosen API.
-   Ensuring data consistency and accuracy when fetching and displaying information from the API.

### c. Security

-   Secure user authentication and password storage.
-   Protect sensitive user data, such as email addresses, from unauthorized access.

### d. Functionality

-   User registration and profile management.
-   Anime search, discovery, and detailed information pages.
-   Watchlist creation and management.
-   User-generated content: reviews, ratings, and comments.
-   Community features: forums and social interactions.
-   News and updates on the anime industry.

### e. User Flow

-   Registration/login process.
-   Anime discovery and watchlist creation.
-   User-generated content creation (reviews, comments).
-   Interactions within the community (forum posts, likes, follows).
-   Personalized recommendations and news feed.
-   Notifications for updates and user interactions.

### More than CRUD

  **Advanced User Profiles**:
    
-   Achievement System: Allow users to earn badges and achievements based on their activity and contributions to the community.

 -   Profile Customization: Let users customize their profiles with avatars, backgrounds, and personal information.

**Social Features**:

-   User Interactions: Enable users to follow each other, create friend lists, and see what anime their friends are watching.
-   Real-time Chat: Incorporate chat functionality for users to discuss anime and related topics in real-time.
