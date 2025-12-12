const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
 * Initializes deletion functionality for the provided delete buttons.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const taskId = e.currentTarget.getAttribute("data-task-id");
        deleteConfirm.href = `${taskId}/delete`;
        deleteModal.show();
    });
}
