import React, {useEffect, useState} from 'react'
import axios from 'axios'

export default function Signals(){
  const [signals, setSignals] = useState([])
  useEffect(()=>{
    axios.get('/api/signals').then(r=>setSignals(r.data.signals)).catch(console.error)
    const iv = setInterval(()=>axios.get('/api/signals').then(r=>setSignals(r.data.signals)).catch(()=>{}), 3000)
    return ()=>clearInterval(iv)
  },[])
  return (
    <div>
      <h2>Signals</h2>
      <ul>
        {signals.map(s=>(
          <li key={s.id}>
            <b>{s.parsed?.symbol||'?'}</b> {s.parsed?.side} | raw: {s.raw}
            <div>TPs: {(s.parsed?.tps||[]).join(', ')}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
