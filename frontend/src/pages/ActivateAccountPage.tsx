import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios';
import { Spin } from 'antd';

const ActivateAccountPage: React.FC = () => {
    const [token] = useSearchParams('token');
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(true);

    const activateAccount = async (activationToken: string) => {
        setIsLoading(true);
        setSuccess(null);
        setError(null);
        try {
            await axios.post(`${import.meta.env.VITE_BACKEND_URL}/user/activate_account/${activationToken}`, {});
            setSuccess('Account activated successfully! You can now log in.');
            console.log(`Account activated with token: ${activationToken}`);
        }
        catch (error) {
            setError('Failed to activate account. ' + error.response.data.detail);
            console.error('Error activating account:', error);
        } finally {
            setIsLoading(false);
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
        <div className='border-2 border-main-blue/20 rounded-xl px-[70px] py-[30px]'>
            <h2 className='text-[28px] font-bold text-center mb-[35px]'>Account Activation</h2>
            {isLoading ? (<div className='flex items-center justify-center h-full'>
                    <Spin /><p className='text-center ml-4'>Activating your account, please wait. This can take a few seconds</p>
                </div>
            ) : (
                <>
                    {error && <p className='text-red-500 text-center'>{error}</p>}
                    {success && <p className='text-green-500 text-center'>{success}</p>}
                </>
            )}
        </div>
    </div>
}

export default ActivateAccountPage;