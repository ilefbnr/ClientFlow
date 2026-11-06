
import { useEffect, useState } from "react";
import {
  RefreshCw,
  Users,
  Plus,
  X,
  Pencil,
  Trash2,
} from "lucide-react";

import {
  getCustomers,
  createCustomer,
  updateCustomer,
  deleteCustomer,
} from "../api/customers";

import type { CustomerCreate } from "../api/customers";
import type { Customer } from "../types";
import CustomerForm from "../components/CustomerForm";

function CustomersPage() {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [showForm, setShowForm] = useState(false);
  const [selectedCustomer, setSelectedCustomer] =
    useState<Customer | null>(null);

  // Retrieve customers
  const fetchCustomers = async () => {
    try {
      setLoading(true);
      setError(null);

      const data = await getCustomers();
      setCustomers(data);
    } catch (err) {
      console.error("Customers error:", err);
      setError("Unable to retrieve customers.");
    } finally {
      setLoading(false);
    }
  };

  // Create a customer
  const handleCreateCustomer = async (data: CustomerCreate) => {
    await createCustomer(data);
    await fetchCustomers();
    setShowForm(false);
  };

  // Update a customer
  const handleUpdateCustomer = async (data: CustomerCreate) => {
    if (!selectedCustomer) return;

    await updateCustomer(selectedCustomer.id, data);
    await fetchCustomers();

    setSelectedCustomer(null);
  };

  // Delete a customer
  const handleDeleteCustomer = async (customer: Customer) => {
    const confirmed = window.confirm(
      `Are you sure you want to delete ${customer.full_name}?`
    );

    if (!confirmed) return;

    try {
      await deleteCustomer(customer.id);
      await fetchCustomers();
    } catch (err) {
      console.error("Delete customer error:", err);
      setError("Unable to delete customer.");
    }
  };

  useEffect(() => {
  let isMounted = true;

  getCustomers()
    .then((data) => {
      if (isMounted) {
        setCustomers(data);
      }
    })
    .catch((err) => {
      console.error("Customers error:", err);

      if (isMounted) {
        setError("Unable to retrieve customers.");
      }
    })
    .finally(() => {
      if (isMounted) {
        setLoading(false);
      }
    });

  return () => {
    isMounted = false;
  };
  }, []);

  return (
    <main>
      <div className="page-heading">
        <div>
          <h1>Customers</h1>
          <p>Manage your customer database.</p>
        </div>

        <div className="page-actions">
          <button
            className="refresh-button"
            onClick={fetchCustomers}
            disabled={loading}
          >
            <RefreshCw size={16} />
            Refresh
          </button>

          <button
            className="add-button"
            onClick={() => setShowForm(true)}
          >
            <Plus size={18} />
            Add Customer
          </button>
        </div>
      </div>

      <section className="customer-section">
        <div className="section-heading">
          <div>
            <Users size={20} />
            <h2>All Customers</h2>
          </div>

          <span>{customers.length} customers</span>
        </div>

        {loading ? (
          <p className="state-message">Loading customers...</p>
        ) : error ? (
          <p className="error-message">{error}</p>
        ) : customers.length === 0 ? (
          <p className="state-message">No customers found.</p>
        ) : (
          <div className="table-wrapper">
            <table className="customer-table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Phone</th>
                  <th>Created At</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {customers.map((customer) => (
                  <tr key={customer.id}>
                    <td>{customer.full_name}</td>
                    <td>{customer.email}</td>
                    <td>{customer.phone || "—"}</td>
                    <td>
                      {new Date(
                        customer.created_at
                      ).toLocaleDateString()}
                    </td>

                    <td>
                      <div className="customer-actions">
                        <button
                          className="edit-button"
                          onClick={() => setSelectedCustomer(customer)}
                          title="Edit customer"
                        >
                          <Pencil size={16} />
                        </button>

                        <button
                          className="delete-button"
                          onClick={() => handleDeleteCustomer(customer)}
                          title="Delete customer"
                        >
                          <Trash2 size={16} />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {/* Create Customer Modal */}
      {showForm && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <div>
                <h2>Add Customer</h2>
                <p>Enter the customer's information.</p>
              </div>

              <button
                className="close-button"
                onClick={() => setShowForm(false)}
              >
                <X size={20} />
              </button>
            </div>

            <CustomerForm
              onSubmit={handleCreateCustomer}
              onCancel={() => setShowForm(false)}
            />
          </div>
        </div>
      )}

      {/* Update Customer Modal */}
      {selectedCustomer && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <div>
                <h2>Edit Customer</h2>
                <p>Update the customer's information.</p>
              </div>

              <button
                className="close-button"
                onClick={() => setSelectedCustomer(null)}
              >
                <X size={20} />
              </button>
            </div>

            <CustomerForm
              key={selectedCustomer.id}
              initialData={selectedCustomer}
              onSubmit={handleUpdateCustomer}
              onCancel={() => setSelectedCustomer(null)}
            />
          </div>
        </div>
      )}
    </main>
  );
}

export default CustomersPage;
