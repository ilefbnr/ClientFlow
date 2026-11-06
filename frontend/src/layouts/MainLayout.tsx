
import {
  LayoutDashboard,
  Users,
  Ticket,
  MessageSquare,
  Settings,
  Headset,
} from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";

function MainLayout() {
  const navigation = [
    { label: "Dashboard", path: "/", icon: LayoutDashboard },
    { label: "Customers", path: "/customers", icon: Users },
    { label: "Tickets", path: "/tickets", icon: Ticket },
    { label: "Conversations", path: "/conversations", icon: MessageSquare },
  ];

  return (
    <div className="app-layout">
      <aside className="sidebar">
        <div className="brand">
          <Headset size={28} />
          <span>ClientFlow</span>
        </div>

        <p className="nav-heading">WORKSPACE</p>

        <nav>
          {navigation.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                end={item.path === "/"}
                className={({ isActive }) =>
                  `nav-item ${isActive ? "active" : ""}`
                }
              >
                <Icon size={20} />
                <span>{item.label}</span>
              </NavLink>
            );
          })}
        </nav>

        <div className="sidebar-bottom">
          <div className="nav-item">
            <Settings size={20} />
            <span>Settings</span>
          </div>
        </div>
      </aside>

      <div className="main-content">
        <header className="topbar">
          <span>Workspace / ClientFlow</span>
          <div className="user-avatar">A</div>
        </header>

        <div className="page-content">
          <Outlet />
        </div>
      </div>
    </div>
  );
}

export default MainLayout;
