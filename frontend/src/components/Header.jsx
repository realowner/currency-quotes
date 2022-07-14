import React from 'react';

const Header = () => {
    return (
        <div className='header'>
            <div>
                <h1>Currency Quotas</h1>
                <p>Веб приложение для API</p>
            </div>
            <div className='header-links'>
                <div>
                    <h1>EvSE</h1>
                    <p>13.08.22</p>
                </div>
                <a href="https://github.com/realowner">
                    <img src="images/github.png" alt="" className='github-logo'/>
                </a>
            </div>
        </div>
    );
};

export default Header;