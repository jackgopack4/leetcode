import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq1 = []
        pq2 = []
        heapify(pq1)
        heapify(pq2)
        lp = 0
        rp = len(costs)-1
        for i in range(0,candidates):
            heappush(pq1,costs[i])
        lp = candidates
        if lp > (len(costs)-candidates):
            stop_index = lp-1
        else:
            stop_index = len(costs)-1-candidates
        for i in range(len(costs)-1,stop_index,-1):
            heappush(pq2,costs[i])
            rp -= 1
        can_sum = 0
        count_workers = 0
        while(count_workers < k):
            if pq2:
                tmp1 = pq1[0]
                tmp2 = pq2[0]
                #print('can from pq1 = %d, from pq2 = %d' % (tmp1,tmp2))
                if lp <= rp:
                    if tmp1 <= tmp2:
                        can_sum += heapreplace(pq1,costs[lp])
                        #print('can_sum = %d'%can_sum)
                        lp += 1
                    else:
                        can_sum += heapreplace(pq2,costs[rp])
                        #print('can_sum = %d'%can_sum)
                        rp -= 1
                else:
                    if pq2:
                        pq1 = list(merge(pq1,pq2))
                        heapify(pq1)
                        pq2.clear()
                    can_sum += heappop(pq1)
                    #print('can_sum = %d'%can_sum)
            else:
                can_sum += heappop(pq1)
                #print('can_sum = %d'%can_sum)
            count_workers += 1
        return can_sum
