
import { useRouter } from 'next/router'
import useSWR from 'swr'
import Layout from '../../components/Layout'
const fetcher = url => fetch(url).then(r => r.json())

export default function Company() {
  const router = useRouter()
  const { id } = router.query
  const api = process.env.API_BASE_URL || 'http://localhost:10000'
  const { data } = useSWR(id ? api + '/api/companies/' + id : null, fetcher)
  if (!data) return <Layout><div>Loading...</div></Layout>
  const company = data
  return (
    <Layout>
      <h2>{company.name} {company.ticker && `(${company.ticker})`}</h2>
      <p>{company.industry} • {company.headquarters}</p>
      <section>
        <h3>Overview</h3>
        <p>{company.description}</p>
      </section>

      <script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify({
        "@context":"https://schema.org",
        "@type":"Organization",
        "name": company.name,
        "url": company.website,
        "logo": company.logo_url,
        "sameAs": company.website
      })}} />
    </Layout>
  )
}
