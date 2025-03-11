"use client";

import styles from "./TaskCard.module.css";
import {
  completeTask,
  incompleteTask,
  deleteTask,
} from "@/actions/taskActions";

export default function TaskCard({
  task,
  onUpdate,
  onComplete,
  onIncomplete,
  onDelete,
}) {
  const { id, title, completed, created_at, completed_at } = task;

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const time = date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    });
    const day = date.toLocaleDateString([], {
      day: "numeric",
      month: "short",
      year: "numeric",
    });
    return `${time} - ${day}`;
  };

  const handleComplete = async () => {
    try {
      await completeTask(id);
      onComplete();
    } catch (error) {
      console.error("Error completing task:", error);
    }
  };

  const handleIncomplete = async () => {
    try {
      await incompleteTask(id);
      onIncomplete();
    } catch (error) {
      console.error("Error marking task as incomplete:", error);
    }
  };

  const handleDelete = async () => {
    try {
      await deleteTask(id);
      onDelete();
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };

  return (
    <div className={styles.card}>
      <div className={styles.content}>
        <h3 className={completed ? styles.completedTitle : styles.title}>
          {title}
        </h3>
        <div className={styles.dates}>
          <p>Created: {formatDate(created_at)}</p>
          {completed && completed_at && (
            <p>Completed: {formatDate(completed_at)}</p>
          )}
        </div>
      </div>
      <div className={styles.actions}>
        {!completed && (
          <button
            className={`${styles.button} ${styles.updateButton}`}
            onClick={onUpdate}
          >
            Update
          </button>
        )}
        {!completed ? (
          <button
            className={`${styles.button} ${styles.completeButton}`}
            onClick={handleComplete}
          >
            Complete
          </button>
        ) : (
          <button
            className={`${styles.button} ${styles.incompleteButton}`}
            onClick={handleIncomplete}
          >
            Undo
          </button>
        )}
        <button
          className={`${styles.button} ${styles.deleteButton}`}
          onClick={handleDelete}
        >
          Delete
        </button>
      </div>
    </div>
  );
}
