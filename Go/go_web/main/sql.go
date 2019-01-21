package main

import "context"

const (
	getAllByProductIDAndCustomerID = `select * from p_orders where product_id in (:product_id) and customer_id=:customer_id`
)

// GetAllByProductIDAndCustomerID
// @param driver_id
// @param rate_date
// @return []Order, error
func GetAllByProductIDsAndCustomerID(ctx context.Context, productIDs []uint64, customerID uint64) ([]Order, error) {
	var orderList []Order

	params := map[string]interface{}{
		"product_id" : productIDs,
		"customer_id": customerID,
	}

	// getAllByProductIdsAndCustomerID 是 const 类型的 sql 字符串
	sql, args, err := sqlutil.Named(getAllByProductIDsAndCustomerID, params)
	if err != nil {
		return nil, err
	}

	err = dao.QueryList(ctx, sqldbInstance, sql, args, &orderList)
	if err != nil {
		return nil, err
	}

	return orderList, err
}
