import { useRouter } from 'next/router'

const ViewQuery = () => {
    const router = useRouter()
    const { imgid } = router.query
    return <p>Post: {imgid}</p>
}

export default ViewQuery