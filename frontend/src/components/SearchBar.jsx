"use client";

import { useState } from "react";
import styles from "./SearchBar.module.css";

export default function SearchBar({ onSearch }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <form className={styles.searchForm} onSubmit={handleSubmit}>
      <input
        type="text"
        className={styles.searchInput}
        placeholder="Search tasks..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit" className={styles.searchButton}>
        Search
      </button>
    </form>
  );
}
