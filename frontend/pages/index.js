
import useSWR from 'swr'
import Layout from '../components/Layout'
const fetcher = url => fetch(url).then(r => r.json())

export default function Home() {
  const api = process.env.API_BASE_URL || 'http://localhost:10000'
  const { data } = useSWR(api + '/api/companies?limit=10', fetcher)

  return (
    <Layout>
      <h2>Top companies (sample)</h2>
      {!data && <div>Loading...</div>}
      {data && (
        <ul>
          {data.companies.map(c => (
            <li key={c.id}>
              <a href={'/company/' + c.id}>{c.rank ? `#${c.rank} ` : ''}{c.name} {c.ticker ? `(${c.ticker})` : ''}</a>
            </li>
          ))}
        </ul>
      )}
    </Layout>
  )
}
