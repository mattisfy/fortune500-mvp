
export default function Layout({children}) {
  return (
    <div style={{fontFamily:'system-ui, Arial', maxWidth:1100, margin:'0 auto', padding:20}}>
      <header style={{display:'flex', justifyContent:'space-between', alignItems:'center', marginBottom:20}}>
        <h1 style={{margin:0}}>Fortune 500 DB</h1>
        <nav>
          <a href="/" style={{marginRight:12}}>Home</a>
          <a href="/browse" style={{marginRight:12}}>Browse</a>
          <a href="/companies" style={{marginRight:12}}>Companies</a>
          <a href="/people">People</a>
        </nav>
      </header>
      <main>{children}</main>
      <footer style={{marginTop:40, color:'#666'}}>Built for AI-friendly search • JSON-LD on pages</footer>
    </div>
  )
}
