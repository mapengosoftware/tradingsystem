import React from 'react'
import Signals from './components/Signals'
import Orders from './components/Orders'

export default function App(){
  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h1>Trading Dashboard - Demo</h1>
      <div style={{display:'flex', gap:20}}>
        <div style={{flex:1}}>
          <Signals />
        </div>
        <div style={{flex:1}}>
          <Orders />
        </div>
      </div>
    </div>
  )
}
