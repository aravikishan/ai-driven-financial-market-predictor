import React from 'react';
import axios from 'axios';

function App() {
  const [prices, setPrices] = React.useState([]);

  React.useEffect(() => {
    axios.get('/api/prices/AAPL').then(response => {
      setPrices(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Stock Prices</h1>
      <ul>
        {prices.map(price => <li key={price.id}>{price.ticker}: {price.price}</li>)}
      </ul>
    </div>
  );
}

export default App;
