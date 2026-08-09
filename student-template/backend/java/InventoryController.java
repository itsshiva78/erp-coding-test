package com.erp.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;
import java.util.Map;

@RestController
public class InventoryController {

    // TODO: Inject JdbcTemplate here
private final JdbcTemplate jdbcTemplate;

    public InventoryController(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    /**
     * TODO: Implement this method.
     * 1. Query 'inventory' table where quantity <= reorder_level.
     * 2. Return List of Maps representing JSON objects.
     */
    @GetMapping("/api/inventory/alerts")
    public List<Map<String, Object>> getAlerts() {
        String sql = """
                SELECT *
                FROM inventory
                WHERE quantity <= reorder_level
                """;

        return jdbcTemplate.queryForList(sql);
        throw new UnsupportedOperationException("Not implemented yet");
    }
}
