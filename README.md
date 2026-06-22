# URL Shortener System

## Project Description

The URL Shortener System is a web/mobile application designed to convert long URLs into shorter, easier-to-share links. The system stores the original URL and generates a unique short code that redirects users to the intended destination when accessed. It also provides basic analytics to monitor link usage and improve link management.

---

## Objectives

* Shorten long URLs into compact links.
* Store and manage URL mappings efficiently.
* Redirect users from short URLs to original URLs.
* Track link usage through click analytics.
* Demonstrate the application of data structures and algorithms in solving real-world problems.

---

## Features

* URL shortening
* Unique short code generation
* URL redirection
* Copy-to-clipboard functionality
* Click tracking and analytics
* Link history management
* Collision handling for duplicate short codes

---

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript, Google Chrome
* **Backend:** Node.js, Express.js
* **Database:** MySQL, phpMyAdmin
* **Version Control:** Git, GitHub
* **Tools:** Vs Code, Google Chrome

---

## System Workflow

1. User enters a long URL.
2. The system validates the URL.
3. A unique short code is generated.
4. The system checks for collisions and generates a new code if necessary.
5. The URL mapping is stored in the database.
6. The shortened URL is displayed to the user.
7. When the short URL is accessed, the system redirects the user to the original URL.
8. Click statistics are recorded for analytics.

---

## Data Structures and Algorithms Used

### Data Structures

* **Hash Table** – Fast storage and retrieval of URL mappings.
* **Queue** – Handles URL processing requests.
* **Stack** – Supports undo/history operations.
* **Heap** – Ranks popular URLs based on click counts.
* **Graph** – Analyzes relationships between shared URLs and users.

### Algorithms

* **Binary Search** – Efficient searching of sorted URL records.
* **Merge Sort** – Sorting URLs and analytics data efficiently.

---

## Team Members and Responsibilities

* **Member 1 – Team Leader & Integration**
* Cecily Ado - BIT/2024/73846

  * Coordinates project activities
  * Manages GitHub repository
  * Oversees integration of all system components

* **Member 2 – Backend & Database Developer**
* JoyAnne Wanjiku - BIT/2024/57080

  * Develops backend functionality
  * Creates APIs and business logic
  * Designs and manages the database

* **Member 3 – Data Structures & Algorithms Developer**
* Haron Mutai - BIT/2024/73474

  * Implements data structures and algorithms
  * Designs collision handling mechanisms
  * Performs complexity and scalability analysis

* **Member 4 – Frontend/UI Developer**
* Beyonce Ngao - BIT/2024/74225

  * Designs and develops the user interface
  * Connects frontend components to backend services
  * Ensures a user-friendly experience

* **Member 5 – Testing, Documentation & Video Lead**
* Caleb Nthiga - BIT/2024/55790

  * Conducts system testing
  * Prepares project documentation
  * Records and edits the project demonstration video

---

## Expected Outcomes

* Functional URL shortening service.
* Efficient URL storage and retrieval.
* Effective collision handling mechanism.
* User-friendly interface.
* Analytics dashboard for monitoring link usage.
* Comprehensive project documentation.

---

## Acknowledgement of AI Use

Artificial Intelligence (AI) was used as a learning and research aid during the development of this project. AI assisted in understanding data structures, algorithms, system design concepts, and complexity analysis. All project decisions, implementation, review, testing, and final presentation were completed by the project team.
