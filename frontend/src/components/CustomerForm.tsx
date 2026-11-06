
import { useState } from "react";
import type { FormEvent } from "react";
import type { CustomerCreate } from "../api/customers";

interface CustomerFormProps {
  onSubmit: (data: CustomerCreate) => Promise<void>;
  onCancel: () => void;
}

function CustomerForm({ onSubmit, onCancel }: CustomerFormProps) {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
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
    } catch (err: any) {
      const status = err.response?.status;

      if (status === 409) {
        setError("This email address is already registered.");
      } else if (status === 422) {
        setError("Please check the information you entered.");
      } else {
        setError("Unable to create customer. Please try again.");
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
          placeholder="Enter customer name"
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
          placeholder="customer@example.com"
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
          placeholder="+216 XX XXX XXX"
        />
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="form-actions">
        <button type="button" onClick={onCancel} disabled={loading}>
          Cancel
        </button>

        <button type="submit" disabled={loading}>
          {loading ? "Creating..." : "Create Customer"}
        </button>
      </div>
    </form>
  );
}

export default CustomerForm;
