import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  useEffect(() => {
    const endpoint = `${process.env.REACT_APP_CODESPACE_URL}/api/activities/`;
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      });
  }, []);
  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={idx}>
                  <td>{activity.name || '-'}</td>
                  <td>{activity.type || '-'}</td>
                  <td>{activity.date || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
export default Activities;
