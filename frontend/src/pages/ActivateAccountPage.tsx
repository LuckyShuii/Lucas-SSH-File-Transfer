import React, { useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios';

const ActivateAccountPage: React.FC = () => {
    const [token, setToken] = useSearchParams('token');

    const activateAccount = async (activationToken: string) => {
        try {
            await axios.post(`${import.meta.env.VITE_BACKEND_URL}/user/activate_account/${activationToken}`, {});
            console.log(`Account activated with token: ${activationToken}`);
        }
        catch (error) {
            console.error('Error activating account:', error);
        }
    };

    useEffect(() => {
        const activationToken = token.get('token');
        if (activationToken) {
            activateAccount(activationToken);
        }
        else {
            console.error('No activation token provided in the URL');
        }
    }, [token]);

    return <div>
        Activate Account PAGE
    </div>
}

export default ActivateAccountPage;