# questions-competition
# Questions API

This API provides questions from the Open Trivia Database. Below are some example endpoints demonstrating different responses based on query parameters.

## Example Endpoints

1. **Without any query parameters:**
   - URL: [http://localhost:3000/api/questions](http://localhost:3000/api/questions)
   - Description: Returns 10 random questions.

2. **With `amount` query parameter:**
   - URL 1: [http://localhost:3000/api/questions?amount=20](http://localhost:3000/api/questions?amount=20)
   - Description: Returns 20 random questions.
   - URL 2: [http://localhost:3000/api/questions?amount=30](http://localhost:3000/api/questions?amount=30)
   - Description: Returns 30 random questions.

3. **With `category` query parameter:**
   - URL 1: [http://localhost:3000/api/questions?category=21](http://localhost:3000/api/questions?category=21)
   - Description: Returns 10 random questions from the Sports category.
   - URL 2: [http://localhost:3000/api/questions?category=23](http://localhost:3000/api/questions?category=23)
   - Description: Returns 10 random questions from the History category.
