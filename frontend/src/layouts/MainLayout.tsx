import LoginPage from '@/pages/LoginPage';
import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import HeaderLayout from './HeaderLayout';
import FooterLayout from './FooterLayout';
import SignUpPage from '@/pages/SignUpPage';
import ActivateAccountPage from '@/pages/ActivateAccountPage';

const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage />,
  },
  {
    path: "/signup",
    element: <SignUpPage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "/activate-account",
    element: <ActivateAccountPage />,
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
