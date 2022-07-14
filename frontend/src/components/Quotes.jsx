import React, { useState, useEffect } from 'react';
import axios from 'axios';
import QuotesItem from './QuotesItem';
import DataTable from './DataTable';


const Quotes = () => {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);
    const [selectedNames, setSelectedNames] = useState([]);

    const [isExport, setIsExport] = useState(false);
    const [exportItems, setExportItems] = useState([]);
    
    const addName = (name) => {
        setSelectedNames([...selectedNames, name]);
    };

    const removeName = (name) => {
        setSelectedNames(selectedNames.filter(n => n !== name));
    };

    async function exportQuotes() {
        const requestOptions = {
            method: "post",
            url: "http://127.0.0.1:8000/quotes/showselected",
            data: selectedNames,
        };
        const apiResponse = await axios(requestOptions);
        setExportItems(apiResponse.data);
        setIsExport(true);
    };

    async function getQuotes() {
        const requestOptions = {
            method: "get",
            url: "http://127.0.0.1:8000/quotes/fromapi",
        };
        await axios(requestOptions);
        window.location.reload();
    };

    useEffect(() => {
        fetch("http://127.0.0.1:8000/quotes/")
        .then(res => res.json())
        .then(
            (result) => {
                setIsLoaded(true);
                setItems(result);
            },
            (error) => {
                setIsLoaded(true);
                setError(error);
            }
        )

        console.log('Выборка валют: ' + selectedNames);
        console.log('Предыдущий экпорт: ' + exportItems.length);
    }, [selectedNames, exportItems]);

    if (error) {
        return <p>Error: {error.message}</p> 
    } else if (!isLoaded) {
        return <p>Loading...</p>
    } else {
        return (
            <div>
                <div className='quotes'>
                    <div className="quotes-tittle">
                        <button className='btn' onClick={getQuotes}>Обновить катировки</button>
                        <div>
                            <h2>Доступные валюты</h2>
                            <p>Данные могут быть устаревшими, рекомендую обновить катировки</p>
                        </div>
                    </div>
                    <div className="quotes-items">
                        {items.map(item => (
                            <QuotesItem item={item} addname={addName} removename={removeName} key={item.id}/>
                        ))}
                    </div>
                    <button className='btn btn-big' onClick={exportQuotes}>Сгенерировать таблицу данных</button>
                </div>
                {isExport
                    ? <DataTable exportData={exportItems}/>
                    : <p className='text-notice'>Для отображения и экспорта данных выберите нужную валюту и сгенирируйте таблицу</p>
                }
            </div>
            
        )
    }
};

export default Quotes;