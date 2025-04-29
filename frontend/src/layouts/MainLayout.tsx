import LoginPage from '@/pages/LoginPage';
import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import HeaderLayout from './HeaderLayout';
import FooterLayout from './FooterLayout';

const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "*",
    element: <h1>404 - Page not found</h1>,
  },
]);

const MainLayout: React.FC = () => {
  return (
    <div className="main-layout">
      <HeaderLayout />
      <div className="content">
        <RouterProvider router={router} />
      </div>
      <FooterLayout />
    </div>
  );
};

export default MainLayout;
