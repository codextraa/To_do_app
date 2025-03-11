"use client";

import styles from "./FilterToggle.module.css";

export default function FilterToggle({ isCompleted, onChange }) {
  return (
    <div className={styles.filterContainer}>
      <span className={styles.label}>Completed:</span>
      <label className={styles.toggle}>
        <input
          type="checkbox"
          checked={isCompleted}
          onChange={(e) => onChange(e.target.checked)}
        />
        <span className={styles.slider}></span>
      </label>
    </div>
  );
}
