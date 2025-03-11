"use client";

import styles from "./CreateButton.module.css";

export default function CreateButton({ onClick }) {
  return (
    <button className={styles.createButton} onClick={onClick}>
      Create Task
    </button>
  );
}
