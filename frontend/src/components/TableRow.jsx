import React from 'react';

const TableRow = (props) => {
    return (
        <tr>
            <th>{props.item.num_code}</th>
            <th>{props.item.name}</th>
            <th>{props.item.price}</th>
            <th>{props.item.date}</th>
            <th>{props.item.nominal}</th>
        </tr>
    );
};

export default TableRow;