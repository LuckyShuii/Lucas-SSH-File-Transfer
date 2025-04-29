import React from 'react';
import type { MenuProps } from 'antd';
import { Dropdown, message, Space, Button } from 'antd';
import { DownOutlined } from '@ant-design/icons';

const onClick: MenuProps['onClick'] = ({ key }) => {
    message.info(`Click on item ${key}`);
};

const items: MenuProps['items'] = [
    {
        label: 'My files',
        key: '1',
    },
    {
        label: 'Account settings',
        key: '2',
    },
    {
        type: 'divider',
    },    
    {
        label: 'Log out',
        key: '3',
        danger: true,
    },
];  

const HeaderLayout: React.FC = () => {
    return <div className='flex justify-between items-center w-full mt-[55px]'>
        <img src='/src/assets/main-logo.svg' alt='Logo' />
        <div className='flex items-center'>
            <h1 className='text-[20px]'>WELCOME <span className='text-main-green'>pseudo</span></h1>
            <Button type='primary' icon={<img src='/src/assets/icons/ssh.svg' />} iconPosition='start' className='!w-[200px] !h-[50px] mx-[23px] !text-[20px]'>Transfer now</Button>
            <Dropdown menu={{ items, onClick }} className='flex items-center' placement="bottom">
                <a onClick={(e) => e.preventDefault()}>
                    <Space>
                        <img src='/src/assets/icons/empty-profile-image.svg' alt='Profile' className='ml-2 w-[55px] h-[55px]'/>
                        <DownOutlined />
                    </Space>
                </a>
            </Dropdown>
        </div>
    </div>
}

export default HeaderLayout;