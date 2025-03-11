"use client";

import { useState, useEffect } from "react";
import { fetchTasks } from "@/actions/taskActions";
import Header from "@/components/Header";
import SearchBar from "@/components/SearchBar";
import FilterToggle from "@/components/FilterToggle";
import CreateButton from "@/components/CreateButton";
import TaskCard from "@/components/TaskCard";
import TaskModal from "@/components/TaskModal";
import styles from "./page.module.css";

export default function TasksPage() {
  const [tasks, setTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");
  const [isCompleted, setIsCompleted] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [currentTask, setCurrentTask] = useState(null);

  const loadTasks = async () => {
    setIsLoading(true);
    try {
      const queryParams = { completed: isCompleted };
      if (searchQuery) queryParams.title = searchQuery;
      const data = await fetchTasks(queryParams);
      setTasks(data);
    } catch (error) {
      console.error("Error fetching tasks:", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, [searchQuery, isCompleted]);

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  const handleFilterChange = (completed) => {
    setIsCompleted(completed);
  };

  const handleCreateClick = () => {
    setCurrentTask(null);
    setShowModal(true);
  };

  const handleUpdateClick = (task) => {
    setCurrentTask(task);
    setShowModal(true);
  };

  const handleModalClose = () => {
    setShowModal(false);
    setCurrentTask(null);
  };

  const handleTaskCreated = () => {
    setShowModal(false);
    loadTasks();
  };

  const handleTaskUpdated = () => {
    setShowModal(false);
    loadTasks();
  };

  const handleTaskCompleted = () => {
    loadTasks();
  };

  const handleTaskIncompleted = () => {
    loadTasks();
  };

  const handleTaskDeleted = () => {
    loadTasks();
  };

  return (
    <div className={styles.container}>
      <Header />
      <div className={styles.controls}>
        <CreateButton onClick={handleCreateClick} />
        <SearchBar onSearch={handleSearch} />
        <FilterToggle isCompleted={isCompleted} onChange={handleFilterChange} />
      </div>

      {isLoading ? (
        <div className={styles.loading}>Loading tasks...</div>
      ) : (
        <div className={styles.taskList}>
          {tasks.length === 0 ? (
            <div className={styles.noTasks}>
              No tasks found.{" "}
              {!isCompleted && "Create a new task to get started!"}
            </div>
          ) : (
            tasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onUpdate={() => handleUpdateClick(task)}
                onComplete={handleTaskCompleted}
                onIncomplete={handleTaskIncompleted}
                onDelete={handleTaskDeleted}
              />
            ))
          )}
        </div>
      )}

      {showModal && (
        <TaskModal
          task={currentTask}
          onClose={handleModalClose}
          onTaskCreated={handleTaskCreated}
          onTaskUpdated={handleTaskUpdated}
        />
      )}
    </div>
  );
}
