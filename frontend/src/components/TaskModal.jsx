"use client";

import { useState, useEffect } from "react";
import styles from "./TaskModal.module.css";
import { createTask, updateTask } from "@/actions/taskActions";

export default function TaskModal({
  task,
  onClose,
  onTaskCreated,
  onTaskUpdated,
}) {
  const [title, setTitle] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const isEditing = !!task;

  useEffect(() => {
    if (task) {
      setTitle(task.title);
    }
  }, [task]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title.trim()) {
      return;
    }

    setIsSubmitting(true);

    try {
      if (isEditing) {
        await updateTask(task.id, { title });
        onTaskUpdated();
      } else {
        await createTask({ title });
        onTaskCreated();
      }
    } catch (error) {
      console.error("Error saving task:", error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className={styles.modalOverlay}>
      <div className={styles.modal}>
        <div className={styles.modalHeader}>
          <h2>{isEditing ? "Update Task" : "Create Task"}</h2>
          <button className={styles.closeButton} onClick={onClose}>
            ×
          </button>
        </div>
        <form onSubmit={handleSubmit}>
          <div className={styles.formGroup}>
            <label htmlFor="title">Task Title</label>
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter task title"
              required
              minLength={1}
              className={styles.input}
            />
          </div>
          <div className={styles.formActions}>
            <button
              type="submit"
              className={styles.submitButton}
              disabled={isSubmitting || !title.trim()}
            >
              {isSubmitting ? "Saving..." : isEditing ? "Update" : "Create"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
