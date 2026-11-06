import { useEffect, useState } from "react";
import {
  Users,
  Ticket,
  MessageSquare,
  AlertTriangle,
  Clock,
  CheckCircle,
} from "lucide-react";

import { getDashboardStats } from "../api/dashboard";
import type { DashboardStats } from "../types";

function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const data = await getDashboardStats();
        setStats(data);
      } catch (err) {
        console.error("Dashboard error:", err);
        setError("Impossible de récupérer les statistiques.");
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return <p>Chargement du Dashboard...</p>;
  }

  if (error || !stats) {
    return <p>{error ?? "Une erreur est survenue."}</p>;
  }

  const cards = [
    {
      title: "Total Customers",
      value: stats.total_customers,
      icon: Users,
    },
    {
      title: "Total Tickets",
      value: stats.total_tickets,
      icon: Ticket,
    },
    {
      title: "Open Tickets",
      value: stats.open_tickets,
      icon: Clock,
    },
    {
      title: "In Progress",
      value: stats.in_progress_tickets,
      icon: AlertTriangle,
    },
    {
      title: "Resolved Tickets",
      value: stats.resolved_tickets,
      icon: CheckCircle,
    },
    {
      title: "Urgent Tickets",
      value: stats.urgent_tickets,
      icon: AlertTriangle,
    },
    {
      title: "Total Conversations",
      value: stats.total_conversations,
      icon: MessageSquare,
    },
    {
      title: "Open Conversations",
      value: stats.open_conversations,
      icon: MessageSquare,
    },
  ];

  return (
    <main>
      <h1>Dashboard</h1>
      <p>Overview of your business activity</p>

      <section className="dashboard-grid">
        {cards.map((card) => {
          const Icon = card.icon;

          return (
            <article className="stat-card" key={card.title}>
              <Icon size={24} />
              <h3>{card.title}</h3>
              <p className="stat-value">{card.value}</p>
            </article>
          );
        })}
      </section>
    </main>
  );
}

export default Dashboard;