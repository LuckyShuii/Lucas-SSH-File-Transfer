import React, { useState } from 'react';
import { Form, Input, Button, Checkbox } from 'antd';
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
import { Icon } from '@iconify/react';
import axios from 'axios';
import { Alert } from 'antd';
import type { SignUpPageProps } from '@/types/SignUpProps';
import { onValuesChange } from '@/components/SignUpPage/onValuesChange';

const SignUpPage: React.FC = () => {
    // State variables to manage form submission and error/success messages
    const [isDisabled, setIsDisabled] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<string | null>(null);
    const [form] = Form.useForm();

    /**
     * onFinish is a callback function that is called when the form is submitted.
     * 
     * @param values values of the form
     */
    const onFinish = async (values: SignUpPageProps) => {
        try {
            // Send a POST request to the server with the form data
            await axios.post(`${import.meta.env.VITE_BACKEND_URL}/user/signup`, {
                username: values.username,
                email: values.email,
                password: values.password,
                rgpd: values.rgpd,
            });

            if (error) {
                // If there is an error, set the error state to null
                setError(null);
            }

            // Set success message state
            setSuccess("Account created successfully. Please check your mailbox to activate your account.");

            // Reset form on submit success
            form.resetFields();
        } catch (error) {
            // Set success message state to null
            setSuccess(null);

            // Set error message state
            setError(error.response.data.detail);
        }
    };

    return (
        <div className='border-2 border-main-blue/20 rounded-xl px-[70px] py-[30px]'>
            <h2 className='text-[28px] font-bold text-center mb-[35px]'>Create an account</h2>
            {/* @onFinish is the function that will be called when the form is submitted */}
            <Form layout="vertical" onFinish={onFinish} className='w-[300px]' onValuesChange={(changed, all) => onValuesChange(changed, all, setIsDisabled)} form={form}>
                
                {/* USERNAME INPUT */}
                <Form.Item
                    name="username"
                    rules={[{ required: true, message: 'Please enter your username' }]}
                    className='!mb-[40px]'
                >
                    <Input
                        placeholder="Username"
                        prefix={<img src='/src/assets/icons/username.svg' className='ml-[-5px] mr-4 w-6' />}
                        variant="underlined"
                    />
                </Form.Item>

                {/* EMAIL INPUT */}
                <Form.Item
                    name="email"
                    rules={[{ required: true, type: 'email', message: 'Please enter a valid email' }]}
                    className='!mb-[40px]'
                >
                    <Input
                        placeholder="Email"
                        prefix={<img src='/src/assets/icons/mail.svg' className='ml-[-5px] mr-4 w-6' />}
                        variant="underlined"
                    />
                </Form.Item>

                {/* PASSWORD INPUT */}
                <Form.Item
                    name="password"
                    rules={[{ required: true, message: 'Please enter your password' }]}
                    className='!mb-[40px]'
                >
                    <Input.Password
                        placeholder="Password"
                        prefix={<img src='/src/assets/icons/password.svg' className='ml-[-5px] mr-4 w-6' />}
                        iconRender={(visible) => visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />}
                        variant="underlined"
                    />
                </Form.Item>

                {/* CONFIRM PASSWORD INPUT */}
                <Form.Item
                    name="confirmPassword"
                    dependencies={["password"]}
                    className='!mb-[35px]'
                    rules={[
                        { required: true, message: 'Please confirm your password' },
                        ({ getFieldValue }) => ({
                            validator(_, value) {
                                if (!value || getFieldValue('password') === value) {
                                    return Promise.resolve();
                                }
                                return Promise.reject(new Error('Passwords do not match'));
                            },
                        }),
                    ]}
                >
                    <Input.Password
                        placeholder="Confirm Password"
                        prefix={<img src='/src/assets/icons/password.svg' className='ml-[-5px] mr-4 w-6' />}
                        iconRender={(visible) => visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />}
                        variant="underlined"
                    />
                </Form.Item>

                {/* RGPD NUMBER CHECKBOX */}
                <Form.Item
                    name="rgpd"
                    valuePropName="checked"
                    rules={[{ required: true, message: 'You must agree to the terms' }]}
                    className='!mb-[30px]'
                >
                    <Checkbox>
                        I agree to the <a href="#" className='text-main-blue'>terms and conditions</a>
                    </Checkbox>
                </Form.Item>

                {/* SUBMIT BUTTON */}
                <Form.Item>
                    <Button
                        type='primary'
                        htmlType='submit'
                        icon={<Icon icon="line-md:login" className='w-[22px]' />}
                        className='!h-[50px] w-full flex items-center justify-center !text-[18px] mb-[-10px]'
                        disabled={isDisabled}
                    >
                        Sign up
                    </Button>
                </Form.Item>

                {/* ERROR MESSAGE */}
                {error && (
                    <Alert
                        description={error}
                        type="error"
                        closable
                        className='!h-[50px] flex !items-center'
                    />
                )}

                {/* SUCCESS MESSAGE */}
                {success && (
                    <Alert
                        description={success}
                        type="success"
                        closable
                    />
                )}
            </Form>
        </div>
    );
};

export default SignUpPage;
export { onValuesChange };