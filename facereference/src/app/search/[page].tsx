import { useRouter } from 'next/router'

const SearchQuery = () => {
    const router = useRouter()
    const { query } = router.query
    return <p>Search query: {query}</p>
}

export default SearchQuery