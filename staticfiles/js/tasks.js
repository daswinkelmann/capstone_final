// const deleteModalElement = document.getElementById("deleteModal");
// const deleteModal = new bootstrap.Modal(deleteModalElement);

// TEMP
console.log("tasks.js loaded");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// TEMP
console.log("found delete buttons:", deleteButtons.length);

/**
 * Initializes deletion functionality for the provided delete buttons.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const taskId = e.currentTarget.getAttribute("data-task-id");
        // TEMP
        console.log("clicked delete for task:", taskId);
        deleteConfirm.href = `${taskId}/delete`;
        deleteModal.show();
    });
}
