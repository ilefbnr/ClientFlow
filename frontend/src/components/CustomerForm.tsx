
import { useState } from "react";
import type { FormEvent } from "react";
import type { Customer } from "../types";
import type { CustomerCreate } from "../api/customers";
import axios from "axios";

interface CustomerFormProps {
  initialData?: Customer;
  onSubmit: (data: CustomerCreate) => Promise<void>;
  onCancel: () => void;
}

function CustomerForm({
  initialData,
  onSubmit,
  onCancel,
}: CustomerFormProps) {
  const [fullName, setFullName] = useState(initialData?.full_name ?? "");
  const [email, setEmail] = useState(initialData?.email ?? "");
  const [phone, setPhone] = useState(initialData?.phone ?? "");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);

    try {
      setLoading(true);

      await onSubmit({
        full_name: fullName.trim(),
        email: email.trim(),
        phone: phone.trim() || null,
      });
    } catch (err: unknown) {
        const status = axios.isAxiosError(err)
          ? err.response?.status
          : undefined;

      if (status === 409) {
        setError("This email address is already registered.");
      } else if (status === 422) {
        setError("Please check the information you entered.");
      } else {
        setError("Unable to save customer. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="customer-form">
      <div className="form-group">
        <label htmlFor="full_name">Full Name *</label>
        <input
          id="full_name"
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="email">Email Address *</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="phone">Phone Number</label>
        <input
          id="phone"
          type="tel"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="form-actions">
        <button type="button" onClick={onCancel} disabled={loading}>
          Cancel
        </button>

        <button type="submit" disabled={loading}>
          {loading
            ? "Saving..."
            : initialData
              ? "Update Customer"
              : "Create Customer"}
        </button>
      </div>
    </form>
  );
}

export default CustomerForm;
