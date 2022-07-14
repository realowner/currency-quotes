import React, { useState } from 'react';

const QuotesItem = (props) => {
    const [checked, setChecked] = useState(false);

    const chengeCheckbox = () => {
        if (checked) {
            props.removename(props.item.name);
        } else {
            props.addname(props.item.name);
        }
        setChecked(!checked);
    }

    return (
        <div className="quote">
            <input type="checkbox" checked={checked} onChange={chengeCheckbox} className='quote-input'/>
            <p>{props.item.name}</p>
        </div>
    );
};

export default QuotesItem;