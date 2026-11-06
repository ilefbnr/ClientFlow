
import apiClient from "./client";
import type { Customer } from "../types";

export interface CustomerCreate {
  full_name: string;
  email: string;
  phone: string | null;
}

// GET: Retrieve all customers
export const getCustomers = async (): Promise<Customer[]> => {
  const response = await apiClient.get<Customer[]>("/customers/");
  return response.data;
};

// POST: Create a customer
export const createCustomer = async (
  data: CustomerCreate
): Promise<Customer> => {
  const response = await apiClient.post<Customer>("/customers/", data);
  return response.data;
};

// PUT: Update a customer
export const updateCustomer = async (
  id: number,
  data: Partial<CustomerCreate>
): Promise<Customer> => {
  const response = await apiClient.put<Customer>(
    `/customers/${id}`,
    data
  );
  return response.data;
};

// DELETE: Delete a customer
export const deleteCustomer = async (id: number): Promise<void> => {
  await apiClient.delete(`/customers/${id}`);
};
