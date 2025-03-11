"use server";

import {
  getTasks as getTasksApi,
  getTask as getTaskApi,
  createTask as createTaskApi,
  updateTask as updateTaskApi,
  deleteTask as deleteTaskApi,
  completeTask as completeTaskApi,
  incompleteTask as incompleteTaskApi,
} from "@/libs/api";

export async function fetchTasks(queryParams = {}) {
  try {
    return getTasksApi(queryParams);
  } catch (error) {
    console.error("Error in fetchTasks action:", error);
    throw new Error("Failed to fetch tasks");
  }
}

export async function fetchTask(id) {
  try {
    return getTaskApi(id);
  } catch (error) {
    console.error("Error in fetchTask action:", error);
    throw new Error("Failed to fetch task");
  }
}

export async function createTask(data) {
  try {
    return createTaskApi(data);
  } catch (error) {
    console.error("Error in createTask action:", error);
    throw new Error("Failed to create task");
  }
}

export async function updateTask(id, data) {
  try {
    return updateTaskApi(id, data);
  } catch (error) {
    console.error("Error in updateTask action:", error);
    throw new Error("Failed to update task");
  }
}

export async function deleteTask(id) {
  try {
    return deleteTaskApi(id);
  } catch (error) {
    console.error("Error in deleteTask action:", error);
    throw new Error("Failed to delete task");
  }
}

export async function completeTask(id) {
  try {
    return completeTaskApi(id, {});
  } catch (error) {
    console.error("Error in completeTask action:", error);
    throw new Error("Failed to complete task");
  }
}

export async function incompleteTask(id) {
  try {
    return incompleteTaskApi(id, {});
  } catch (error) {
    console.error("Error in incompleteTask action:", error);
    throw new Error("Failed to mark task as incomplete");
  }
}
