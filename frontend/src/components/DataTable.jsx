import React from 'react';
import TableRow from './TableRow';

const DataTable = (props) => {
    return (
        <div className='table-block'>
            <table>
                <thead>
                    <tr>
                        <th>Код валюты</th>
                        <th>Название валюты</th>
                        <th>Цена</th>
                        <th>Дата котировки</th>
                        <th>Номинал</th>
                    </tr>
                </thead>
                <tbody>
                    {props.exportData.map(item => (
                        <TableRow item={item} key={item.id}/>
                    ))}
                </tbody>
            </table>
            <div className="table-block-export">
                <p className='text-exp'>Экспортировать как:</p>
                <a href="http://127.0.0.1:8000/quotes/exportpdf" className="btn btn-tbl" target='_blank'>PDF</a>
                <a href="http://127.0.0.1:8000/quotes/exportcsv" className="btn btn-tbl" target='_blank'>CSV</a>
                <a href="http://127.0.0.1:8000/quotes/exportxlsx" className="btn btn-tbl" target='_blank'>XLSX</a>
            </div>
        </div>
    );
};

export default DataTable;