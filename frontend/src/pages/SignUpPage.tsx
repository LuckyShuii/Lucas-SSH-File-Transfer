import React from 'react';
import { Form, Input, Button, Checkbox } from 'antd';
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
import { Icon } from '@iconify/react';

const SignUpPage: React.FC = () => {
const onFinish = (values: any) => {
    console.log('Form submitted:', values);
};

return (
    <div className='border-2 border-main-blue/20 rounded-xl px-[100px] py-[70px]'>
      <h2 className='text-[28px] font-bold text-center mb-[45px]'>Sign up</h2>
      <Form layout="vertical" onFinish={onFinish} className='w-[300px]'>

        {/* USERNAME INPUT */}
        <Form.Item
            name="username"
            rules={[{ required: true, message: 'Please enter your username' }]}
            className='!mb-[50px]'
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
            className='!mb-[50px]'
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
            className='!mb-[50px]'
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
            className='!mb-[50px]'
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
            className='!mb-[40px]'
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
                className='!h-[50px] w-full flex items-center justify-center !text-[18px]'
            >
                Transfer now
            </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default SignUpPage;