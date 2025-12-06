import React, {useEffect, useState} from 'react'
import axios from 'axios'

export default function Orders(){
  const [orders, setOrders] = useState([])
  useEffect(()=>{
    axios.get('/api/orders').then(r=>setOrders(r.data.orders)).catch(console.error)
    const iv = setInterval(()=>axios.get('/api/orders').then(r=>setOrders(r.data.orders)).catch(()=>{}), 3000)
    return ()=>clearInterval(iv)
  },[])
  return (
    <div>
      <h2>Orders</h2>
      <ul>
        {orders.map(o=>(
          <li key={o.id}>
            <b>{o.symbol}</b> {o.side} vol:{o.volume} tp:{o.tp} status:{o.status} fx:{o.fx_id || '-'}
          </li>
        ))}
      </ul>
    </div>
  )
}
