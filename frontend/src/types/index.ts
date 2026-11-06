export interface Customer {
  id: number;
  full_name: string;
  email: string;
  phone: string | null;
  created_at: string;
}

export interface Ticket {
  id: number;
  title: string;
  description: string | null;
  status: "open" | "in_progress" | "resolved" | "closed";
  priority: "low" | "medium" | "high" | "urgent";
  customer_id: number;
  created_at: string;
}

export interface Conversation {
  id: number;
  channel: "email" | "whatsapp" | "messenger" | "phone";
  status: "open" | "closed";
  customer_id: number;
  created_at: string;
}

export interface Message {
  id: number;
  content: string;
  sender_type: "customer" | "business" | "ai_agent";
  conversation_id: number;
  created_at: string;
}

export interface DashboardStats {
  total_customers: number;
  total_tickets: number;
  open_tickets: number;
  in_progress_tickets: number;
  resolved_tickets: number;
  closed_tickets: number;
  urgent_tickets: number;
  total_conversations: number;
  open_conversations: number;
}