# README Framework

## Project Title

_Doodoo – Personal Task Tracker_

## Index

1. Overview
2. UX Design Process
3. Features
4. Improvements and Future Development
5. Deployment
6. Testing and Validation
7. AI Implementation
8. Database
9. References
10. Tech Used
11. Learning Points

---

# 1. Overview

<details>
<summary><strong>Project Scope</strong></summary>

_A simple web app that lets users create, track, and complete personal challenges. It focuses on a clean, mobile-first interface so people can quickly see their challenges, mark them as done, and get a sense of progress over time._

</details>

---

# 2. UX Design Process

<details>
<summary><strong>User Stories</strong></summary>

Core User Stories (MVP)
As a user, I want to register for an account so that I can securely access my personal task list. Acceptance criteria: A registration form is available, valid details create a new account, and the user can log in immediately after registration.


As a user, I want to log in and log out so that my tasks remain private and secure. Acceptance criteria: Only authenticated users can access the app, login validates credentials correctly, logout ends the session and redirects to the login page.


As a user, I want to create a new task so that I can track things I need to do. Acceptance criteria: A task form is available, required fields must be completed, and a newly created task appears in the task list after submission.


As a user, I want to view all my tasks in one place so that I can easily manage my workload. Acceptance criteria: The home screen displays only the logged-in user’s tasks and updates automatically after create, edit, or delete actions.


As a user, I want to edit an existing task so that I can update its details if things change. Acceptance criteria: The edit form is pre-filled with the task’s current data, changes are saved correctly, and the updated task is shown on the task list.


As a user, I want to mark a task as done so that I can track my progress. Acceptance criteria: A visible control allows toggling between To-Do and Done, and the updated status is immediately reflected in the task list.


As a user, I want to delete a task so that I can permanently remove completed or unwanted items. Acceptance criteria: The delete option is available on each task, and confirmed deletion permanently removes the task from the database and task list.


As a user, I want to receive a confirmation before deleting a task so that I do not delete tasks accidentally. Acceptance criteria: A confirmation screen or message appears before deletion and provides options to confirm or cancel the action.


As a user, I want the app to work smoothly on my mobile phone so that I can manage tasks on the go. Acceptance criteria: The layout adapts to mobile screens, buttons are easy to tap, and no horizontal scrolling is required.






Progressive Web App (PWA) User Stories
As a user, I want to install the app on my phone home screen so that it feels like a native mobile app. Acceptance criteria: The app provides a valid manifest file, displays an install prompt on supported devices, and launches in standalone mode when opened from the home screen.


As a user, I want the app to load even when my internet connection is unstable so that I can always access my task list. Acceptance criteria: Core app pages and static assets are cached by a service worker and load successfully when offline.


</details>

<details>
<summary><strong>Wireframes</strong></summary>

_(wireframes or link to PDF)_

</details>

<details>
<summary><strong>Color Scheme</strong></summary>

### Primary Colors

_(Add hex values)_

### Text Colors

_(Add hex values)_

### Background Colors

_(Add hex values)_

### Status Colors

_(colours)_

</details>

<details>
<summary><strong>Fonts</strong></summary>

_fonts_

</details>

---

# 3. Features

<details>
<summary><strong>All Application Features</strong></summary>

_(MVP features)_

</details>

---

# 4. Improvements and Future Development

<details>
<summary><strong>Future Feature Ideas</strong></summary>

_Future features list_

**Progressive Web App (PWA) User Stories**

PWA - install on a phone to seem like a native app
As a user, I want to install the app on my phone home screen so that it feels like a native mobile app. Acceptance criteria: The app provides a valid manifest file, displays an install prompt on supported devices, and launches in standalone mode when opened from the home screen.

PWA 2/2 - App to load on a phone even with no internet connection
As a user, I want the app to load even when my internet connection is unstable so that I can always access my task list. Acceptance criteria: Core app pages and static assets are cached by a service worker and load successfully when offline.


**Future / Nice-to-Have User Stories**

Nice-to-Have - filter by status
As a user, I want to filter tasks by status so that I can focus only on tasks that are still to be completed.
Acceptance Criteria
Users can select a filter option (e.g., All, Completed, Not Completed) and the task list updates instantly to show only matching tasks.
When a filter is active, the UI clearly indicates which filter is applied.


Nice to have - add due dates
As a user, I want to add due dates to tasks so that I can manage deadlines more effectively.
Acceptance Criteria
When creating or editing a task, users can select a due date using a date picker.
Tasks with due dates display that date clearly in the task list.



Nice to have - organise into preset categories
As a user, I want to organise tasks into preset categories so that my task list feels structured.
Acceptance Criteria
Users can choose from a predefined list of categories (e.g., Health, School, Work) when creating or editing a task.

The task list displays each task’s assigned category.


Nice to have - streaks
As a user, I want to track streaks or completion goals so that I stay motivated.
Acceptance Criteria
Completing tasks on consecutive days increases a visible “streak” counter.
The streak counter resets automatically if the user does not complete any tasks in a 24-hour period.


Nice to have - export/backup tasks
As a user, I want to export my tasks so that I can back them up or use them elsewhere.
Acceptance Criteria
Users can tap an “Export” button to download a file (CSV or text) containing all their tasks and statuses.
Exported files include at minimum: task title, status, category, and due date (if used).





</details>

---

# 5. Deployment

<details>
<summary><strong>Deployment Steps</strong></summary>

_Heroku_

</details>

---

# 6. Testing and Validation

<details>
<summary><strong>HTML Validation</strong></summary>
*screenshots/results*  
</details>

<details>
<summary><strong>CSS Validation</strong></summary>
*screenshots/results*  
</details>

<details>
<summary><strong>Python Validation</strong></summary>
*(flake8, pep8, CI Python validator)*  
</details>

<details>
<summary><strong>JavaScript Validation</strong></summary>
*(JS used)*  
</details>

<details>
<summary><strong>Lighthouse</strong></summary>
*(performance score screenshots)*  
</details>

<details>
<summary><strong>Wave (Accessibility)</strong></summary>
*(accessibility results)*  
</details>

<details>
<summary><strong>Manual Testing</strong></summary>
*(Testing table + user flows)*  
</details>

---

# 7. AI Implementation

<details>
<summary><strong>Code Creation</strong></summary>
*(AI - write boilerplate code)*  
</details>

<details>
<summary><strong>Debugging</strong></summary>
*(AI - fix issues)*  
</details>

<details>
<summary><strong>Development Process</strong></summary>
*(AI improved efficiency + workflow)*  
</details>

---

# 8. Database

<details>
<summary><strong>ERD (Entity Relationship Diagram)</strong></summary>
*ERD*  
</details>

<details>
<summary><strong>Main Tables / Models</strong></summary>
*Task model, User model, relationships*  
</details>

---

# 9. References

<details>
<summary><strong>Sources & Credits</strong></summary>
*Links to docs, tutorials, images, icons, etc.*  
</details>

---

# 10. Tech Used

<details>
<summary><strong>Technologies and Tools</strong></summary>
*Django, Python, Bootstrap, GitHub*  
</details>

---

# 11. Learning Points

<details>
<summary><strong>Key Learnings</strong></summary>
*What you learned throughout the project*  
</details>
